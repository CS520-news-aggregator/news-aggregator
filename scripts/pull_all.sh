#!/bin/bash

ls | xargs -P10 -I{} git -C {} pull