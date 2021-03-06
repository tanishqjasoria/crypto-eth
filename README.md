# Ethereum - Elliptic Curves
This repo starts with groups, elliptic curves and build upto kate commitments and Verkle Trees

## Abstract Algebra

## Elliptic Curves

## Elliptic Curve Cryptography
- [A (Relatively Easy To Understand) Primer on Elliptic Curve Cryptography](https://blog.cloudflare.com/a-relatively-easy-to-understand-primer-on-elliptic-curve-cryptography/)
- [Elliptic Curve Cryptography: a gentle introduction](https://andrea.corbellini.name/2015/05/17/elliptic-curve-cryptography-a-gentle-introduction/)
- [Elliptic Curves - Technical Introduction](https://jeremykun.com/2014/02/08/introducing-elliptic-curves/)

## Elliptic Curve Pairings
- [Exploring Elliptic Curve Pairings - Vitalik](https://vitalik.ca/general/2017/01/14/exploring_ecp.html)

## BLS12-381

- [BLS12-381: New zk-SNARK Elliptic Curve Construction](https://electriccoin.co/blog/new-snark-curve/)
- [BLS12-381 For The Rest Of Us](https://hackmd.io/@benjaminion/bls12-381)

## Kate Commitments

- [KZG polynomial commitments - Dankrad](https://dankradfeist.de/ethereum/2020/06/16/kate-polynomial-commitments.html)
- [PCS multiproofs using random evaluation](https://dankradfeist.de/ethereum/2021/06/18/pcs-multiproofs.html)
- [Kate-Zaverucha-Goldberg (KZG) Constant-Sized Polynomial Commitments](https://alinush.github.io/2020/05/06/kzg-polynomial-commitments.html)

## Pederson + IPA

- [Inner Product Arguments](https://dankradfeist.de/ethereum/2021/07/27/inner-product-arguments.html)

## Verkle Trees and State Expiry
- [Verkle Trees - Original Paper](https://math.mit.edu/research/highschool/primes/materials/2018/Kuszmaul.pdf)
- [Verkle Trees - Original Paper - Slides](https://math.mit.edu/research/highschool/primes/materials/2019/conf/12-5-Kuszmaul.pdf)
- [Verkle Trees - Vitalik](https://vitalik.ca/general/2021/06/18/verkle.html)
- [Verkle trie for Eth1 state](https://dankradfeist.de/ethereum/2021/06/18/verkle-trie-for-eth1.html)
- [Verkle Tree - EIP](https://notes.ethereum.org/@vbuterin/verkle_tree_eip)
- [Verkle Tree Structure](https://blog.ethereum.org/2021/12/02/verkle-tree-structure/)
- [State Expiry Summary](https://notes.ethereum.org/@vbuterin/state_expiry_eip)
- [Verkle Tree Summary (Integration)](https://notes.ethereum.org/@vbuterin/verkle_tree_eip)
- [Verkle Tree Structure](https://blog.ethereum.org/2021/12/02/verkle-tree-structure/)
- [Verkle Tree Summary (Integration)](https://notes.ethereum.org/@vbuterin/verkle_tree_eip)

### ETH Related Roadmaps
- [Why it's so important to go stateless](https://dankradfeist.de/ethereum/2021/02/14/why-stateless.html)
- [Ethereum statelessness roadmap](https://notes.ethereum.org/Yn_mwNa2SeeQHnKsRgekKg)
- [A state expiry and statelessness roadmap](https://notes.ethereum.org/@vbuterin/verkle_and_state_expiry_proposal#:~:text=Two%20paths%20to%20a%20solution,witnesses%20to%20revive%20expired%20state)
- [State Expiry Summary](https://notes.ethereum.org/@vbuterin/state_expiry_eip)

### MISC
- [Impact of address space compression proposal (20 byte address: 4 byte prefix, 2 byte period & 14 byte hash), loses address collision resistance](https://ethresear.ch/t/what-would-break-if-we-lose-address-collision-resistance/11356)
- [Fast Fourier Transforms - Vitalik](https://vitalik.ca/general/2019/05/12/fft.html)
- [Stateless Ethereum Meeting 13: Verkle Trees](https://www.youtube.com/watch?v=1hTscLYsaIg)
- [State Expiry - EIP](https://notes.ethereum.org/@vbuterin/state_expiry_eip)
- [State Expiry & Statelessness in Review](https://www.notion.so/State-Expiry-Statelessness-in-Review-8d531abcc2984babb9bf76a44459e611)
- [A few paths to statelessness and state expiry](https://hackmd.io/@vbuterin/state_expiry_paths)
- [Proposed Verkle Tree Scheme for Eth](https://ethereum-magicians.org/t/proposed-verkle-tree-scheme-for-ethereum-state/5805)

### Research implementations of some primitives

- [Verkle](https://github.com/ethereum/research/tree/master/verkle)
- [Verkle Trie](https://github.com/ethereum/research/tree/master/verkle_trie)
- [Verkle Trie Pedersen](https://github.com/ethereum/research/tree/master/verkle_trie_pedersen)
- [KZG Data Availability](https://github.com/ethereum/research/tree/master/kzg_data_availability)
- [In-Place Tree Editing - Vitalik](https://github.com/ethereum/research/blob/master/generic_in_place_tree/tree.py)

### Near production implementation of some primitives

- [go-verkle](https://github.com/gballet/go-verkle)
- [go-kzg](https://github.com/protolambda/go-kzg)
- [rust-verkle](https://github.com/crate-crypto/rust-verkle)
