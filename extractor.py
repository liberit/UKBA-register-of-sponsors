#!/usr/bin/env python

# -*- coding: utf-8 -*-
#    This file is part of liberit.

#    liberit is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    liberit is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with liberit.  If not, see <http://www.gnu.org/licenses/>.

# (C) 2012 Stefan Marsiske <s@ctrlc.hu>

import fileinput, re
from scraptils.utils import jdump

# Organisation Name | Town/City | County | Tier & Rating | Sub Tier

orgre=re.compile(r"^(\S.*?)\s{3,}(\S.*)\s{3,}(\S.*)")
org2re=re.compile(r"^(\S.*?)\s{3,}(\S.*)")
score=re.compile(r"^\s{1,}(\S.*)\s{3,}(\S.*)$")
cache=[]
for line in fileinput.input(openhook=fileinput.hook_compressed):
    m=orgre.match(line)
    if m:
        cache=[x.strip() if x else "" for x in m.groups()]
        continue
    m=org2re.match(line)
    if m:
        cache=[x.strip() if x else "" for x in m.groups()]
        continue
    m=score.match(line)
    if m:
        print jdump({'Organisation Name': cache[0],
                     'Town/City': cache[1],
                     'County': cache[2] if len(cache)>2 else '',
                     'Tier & Rating': m.group(1).strip(),
                     'Sub Tier': m.group(2).strip()}).replace('\n','')
        continue
    #print '[*] alert', cache, line
