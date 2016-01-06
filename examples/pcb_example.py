#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2015 Hamilton Kibbe <ham@hamiltonkib.be>

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

"""
This example demonstrates the use of pcb-tools with cairo to render composite
images using the PCB interface
"""

import os
from gerber import PCB
from gerber.render import GerberCairoContext, theme

GERBER_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), 'gerbers'))


# Create a new drawing context
ctx = GerberCairoContext()

# Create a new PCB
pcb = PCB.from_directory(GERBER_FOLDER)

pcb.theme = theme.THEMES['OSH Park']
ctx.render_layers(pcb.top_layers, os.path.join(os.path.dirname(__file__), 'pcb_top.png'))
ctx.render_layers(pcb.bottom_layers, os.path.join(os.path.dirname(__file__), 'pcb_bottom.png'))

