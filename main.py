#    Copyright 2024 AnnTimcio
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#  limitations under the License.
import logging

from engine import Engine
from word_dict import WordDict

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    eng = Engine()
    wd = WordDict()
    win = []
    words = wd.get_words(20)
    for w in words:
        if eng.add(w):
            win.append(w)
    eng.table.fill_with_random()
    print(eng.table.to_string())
    print(win)
    print(len(win))
