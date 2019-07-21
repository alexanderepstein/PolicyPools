#!/usr/bin/env bash
# MIT License
#
# Copyright (c) 2019 Alex Epstein

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

package_name="policypools"
echo -n "Packaging $package_name into wheel.."
version=$(cat __version__.py | grep -Eo "[0-9.]*" | grep -v "^[.]")
python3 setup.py bdist_wheel --python-tag=py3 > /dev/null || { echo "Failure!"; exit 1; } &

while [ ! -f dist/$package_name-$version-py3-none-any.whl ];do
  echo -n "."
  sleep .5
done
echo -e "Success!\n"


echo -n "Uploading wheel to PyPi..."
twine upload dist/$package_name-$version-py3-none-any.whl > /dev/null || { echo "Failure!"; exit 1; }
echo "Success!"