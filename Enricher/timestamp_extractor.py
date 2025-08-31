from datetime import date
import re
from typing import Optional

class TimestampExtractor:

    _PATTERNS = [
        re.compile(r"\b(?P<d>\d{1,2})[\/\-\.](?P<m>\d{1,2})[\/\-\.](?P<y>\d{4})\b"),
        re.compile(r"\b(?P<y>\d{4})[\/\-](?P<m>\d{1,2})[\/\-](?P<d>\d{1,2})\b"),
    ]

    def extract(self, text: str) -> str:
        if not text:
            return ""
        latest: Optional[date] = None

        for pat in self._PATTERNS:
            for m in pat.finditer(text):
                y = int(m.group("y"))
                mo = int(m.group("m"))
                d = int(m.group("d"))
                try:
                    dt = date(y, mo, d)
                    if latest is None or dt > latest:
                        latest = dt
                except ValueError:
                    continue

        return latest.strftime("%Y-%m-%d") if latest else ""
