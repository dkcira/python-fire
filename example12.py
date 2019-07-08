#!/usr/bin/env python3
# argument parsing
import fire

fire.Fire(lambda obj: type(obj).__name__)