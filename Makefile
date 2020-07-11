#
#  Makefile
#
#  Copyright 2019 Base4 Sistemas Ltda ME
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

.PHONY: main clean fullclean test docs

main:
	@echo "Makefile do projeto SATComum para Python"

clean:
	find . -type d -name '__pycache__' -exec rm -rv {} +
	find . -type d -name '.cache' -exec rm -rv {} +
	find . -type d -name '.pytest_cache' -exec rm -rv {} +
	find . -type d -name 'satcomum.egg-info' -exec rm -rv {} +
	find . -name '*.pyc' -delete -print

fullclean: clean
	find . -type d -path './dist' -exec rm -rv {} +
	find . -type d -path './build' -exec rm -rv {} +
	find . -type d -path './docs/_build' -exec rm -rv {} +
	find . -type d -path './.eggs' -exec rm -rv {} +

test: clean
	pytest

docs: clean
	cd docs && $(MAKE) html
