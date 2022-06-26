import json
import codecs
from settings import CHECKED_APARTMENTS_FILE


class FileUtils(object):

    def get_checked_apartments(self) -> list:
        with codecs.open(CHECKED_APARTMENTS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    def set_checked_apartments(self, data) -> None:
        with codecs.open(CHECKED_APARTMENTS_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, sort_keys=True, indent=2, ensure_ascii=False)
