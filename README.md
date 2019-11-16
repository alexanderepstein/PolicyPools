<div align="center">

# PolicyPools

#### Thread and Process Pools With Policies

</div>

## Install

```bash
pip3 install policypools
```

## Usage
Similar to a Pool executor, in the fact that you submit jobs to be done by the pool. In this case however all jobs must be background tasks
as submissions do not return results. This library uses policies to determine how the cases will be handled when we have maximum concurrent workers 
already running and the pre work queue is full.

Example case 
```python
def some_long_func(id):
    sleep(20)
    print(id)

policy_pool = PolicyThreadPoolFactory.get_policy_pool(policy=Policies.discard_oldest, max_q_size=1, max_workers=1)
for i in range(6):
    policy_pool.submit(target=some_long_func, args=(i, ))
```
The output will be 
```
0
5
```
This is because at each iteration of submission we discarded the oldest worker in the pre work queue. 


There are many reasons why policy behavior in general is useful. 
For discard oldest policy as used in this example is usually useful when a new submission should take precedence 
over an older one as the older one might be working off of stale data and preventing the new workers from running.

### Policies

#### Discard Newest Policy
If a new submission takes place and all of the workers are full along with the pre work queue then discard the newest submission from pre work queue.


#### Discard Oldest Policy
If a new submission takes place and all of the workers are full along with the pre work queue then discard the oldest submission from pre work queue.

#### Discard This Policy
If a new submission takes place and all of the workers are full along with the pre work queue then drop the submitted worker.

## License

MIT License

Copyright (c) 2019 Alex Epstein

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.