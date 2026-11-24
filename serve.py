from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import argparse
import webbrowser
from threading import Lock
from urllib.parse import urlsplit
from xml.etree.ElementTree import ParseError

from export_maps import export


class LocalHandler(SimpleHTTPRequestHandler):
    export_lock = Lock()

    def send_head(self):
        requested = urlsplit(self.path).path
        if requested in ('/assets/tilemaps/maps/level.json',
                         '/assets/tilemaps/maps/finale.json'):
            target = Path(self.directory) / requested.lstrip('/')
            source = target.with_suffix('.tmx')
            try:
                with self.export_lock:
                    dependencies = [source, Path(__file__).with_name('export_maps.py')]
                    dependencies.extend((Path(self.directory) / 'assets/tilemaps').rglob('*.tsx'))
                    if not target.exists() or any(
                        dependency.stat().st_mtime_ns > target.stat().st_mtime_ns
                        for dependency in dependencies
                    ):
                        export(source)
            except (OSError, ValueError, AttributeError, ParseError) as error:
                self.send_error(500, 'Map export failed', str(error))
                return None
        return super().send_head()

    def log_message(self, format, *args):
        pass

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()


class LocalServer(ThreadingHTTPServer):
    allow_reuse_address = False


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--open", action="store_true")
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    handler = partial(LocalHandler, directory=str(root))
    for port in range(4000, 4100):
        try:
            server = LocalServer(("127.0.0.1", port), handler)
            break
        except OSError as error:
            if error.winerror not in (10048, 10013):
                raise
    else:
        raise RuntimeError("No free preview port between 4000 and 4099.")
    with server:
        url = "http://127.0.0.1:{}/".format(server.server_port)
        print("Super Sara: " + url, flush=True)
        if args.open:
            webbrowser.open(url)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
