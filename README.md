<div align="center">

# PolicyPools

<img src="https://i.postimg.cc/2SnB0272/threads-fixed.png">

#### Thread Pool Excecutors With Policies

</div>

## Install

```bash
pip3 install policypools
```

## Usage

Used almost identically to a typical ThreadPoolExecutor, but with a policy. The selected policy will change behavior of the submit call made to the given Policy Thread Pool Executor.

### Policies
Each policy has two parameters:

max_q_size is the max size of the pre work queue or the number of threads that can be queued up to run when possible

max_workers is the max number of concurrently running threads

#### Bounded Policy
If a new submission takes place and all of the workers are full along with the pre work queue then this will raise a RuntimeError.

[Example](https://github.com/alexanderepstein/policypools/blob/master/examples/BoundedPolicyExample.py)

#### Discard Newest Policy
If a new submission takes place and all of the workers are full along with the pre work queue then discard the newest submission from pre work queue.

[Example](https://github.com/alexanderepstein/policypools/blob/master/examples/DiscardNewestPolicyExample.py)

#### Discard Oldest Policy
If a new submission takes place and all of the workers are full along with the pre work queue then discard the oldest submission from pre work queue.

[Example](https://github.com/alexanderepstein/policypools/blob/master/examples/DiscardOldestPolicyExample.py)

#### Infinite Policy
All submissions should be successful, the queue size is infinite and the number of workers is based off of computer specs.

[Example](https://github.com/alexanderepstein/policypools/blob/master/examples/InfinitePolicyExample.py)

## Donate
If this project helped you in any way and you feel like supporting me


[![Donate](https://img.shields.io/badge/Donate-Venmo-blue.svg)](https://venmo.com/AlexanderEpstein)
[![Donate](https://img.shields.io/badge/Donate-SquareCash-green.svg)](https://cash.me/$AlexEpstein)

###### BTC: 38Q5VbH63MtouxHu8BuPNLzfY5B5RNVMDn
###### ETH: 0xf7c60C06D298FF954917eA45206426f79d40Ac9D
###### LTC: LWZ3T19YUk66dgkczN7dRhiXDMqSYrXUV4
###### DSH: XpV1LtM5PvpfR9z5pYFZVmgcpLkDmrFAKM
###### XRP: r4ZsnoHM94zMb2SCJ89fYzQqmGgozqLZF1
###### XLM: GDN7WCUBAKLLUYENLUBM6LA647UAS5QTZDNV3QZMMMQLOJJKPJKACJ3H

## License

MIT License

Copyright (c) 2019 Alex Epstein

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.