"""
Copyright 2017-2019 Fizyr (https://fizyr.com)
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""


def import_package(name, package_type):
	try:
		package = __import__(package_type, fromlist=[name])
		package = getattr(package, name)
	except ImportError:
		raise(name + ' is not present in ' + package_type)

	return package
