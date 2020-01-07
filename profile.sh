#!/bin/bash

for i in `seq 1 30`; do \
ab -n30000 -c$i http://192.168.99.104:30275/en.wikipedia.org/v1/feed/onthisday/all/01/15; \
done