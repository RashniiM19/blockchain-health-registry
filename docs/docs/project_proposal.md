MediChain-ID: Detailed Project Proposal

1. Introduction

This document provides an in-depth look at the architecture, a detailed user flow, and the technical implementation plan for MediChain-ID. The project addresses a fundamental human rights issue: the right to a legal identity. By leveraging a high-performance blockchain like Algorand, we can provide a tamper-proof and accessible solution with extremely low transaction fees.

2. System Architecture Diagram

User Layer:Community Health Worker (CHW) via Mobile App, Individuals via Mobile Wallet.
Application Layer: React Frontend, Node.js Backend.
Blockchain Layer: Algorand Smart Contracts (PyTeal).
Storage Layer:IPFS for encrypted data.

3. User Flow Diagrams

Flow 1: Community Health Worker Birth Registration
1.  CHW opens app.
2.  CHW fills out birth registration form.
3.  App encrypts data and hashes it.
4.  App calls `register_birth` function on smart contract.
5.  Transaction is sent to the Algorand network, which is mined and finalized in seconds.
6.  CHW receives a success confirmation and the transaction ID.

Flow 2: Individual Accessing Records
1.  Individual opens their digital wallet.
2.  Wallet uses their private key to authenticate.
3.  Wallet queries their DID on the blockchain to find associated VCs.
4.  Wallet retrieves the encrypted VC from IPFS.
5.  User can now view their birth certificate or health record.
