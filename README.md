# blockchain-health-registry
A decentralized, blockchain-backed registry for secure, immutable birth and health records. Built for hackathon.
# MediChain-ID: A Blockchain-Backed Community Birth and Health Registry

MediChain-ID: A Blockchain-Backed Community Birth and Health Registry

The Problem

In countless communities around the world, birth and health records are still managed through antiquated, paper-based systems. This leads to a critical set of problems:
* Data Loss & Damage: Paper records are vulnerable to fire, floods, and natural decay.
* Inaccessibility: Records are physically stored and difficult to access, especially in emergencies or for migration.
* Fraud & Manipulation: Paper-based and centralized digital systems are susceptible to fraudulent entries.
* Lack of Identity: A significant portion of the population remains "unregistered," unable to prove their existence or access essential services.

The Solution

MediChain-ID is a decentralized, blockchain-powered platform designed to provide a secure, immutable, and accessible digital identity for individuals from the moment of birth. By leveraging the Algorand blockchain, we can create a single source of truth for birth and health records, empowering individuals with ownership and control over their own data in an eco-friendly and highly scalable environment.

Key Features (MVP for Hackathon)

* Decentralized Identity (DID): Each individual receives a unique, self-sovereign digital identity from birth, not controlled by any central authority.
* On-Chain Birth Registry: An Algorand smart contract (called an **Application**) records an immutable hash of a newborn's key details, creating a permanent, verifiable record of their existence.
*  Immutable Health Records: Subsequent health events are appended as verifiable history to the individual's on-chain record through a series of application calls.
* User-Controlled Access: Individuals, via a secure wallet like Pera Wallet, can grant or revoke access to their records.

Technology Stack

* Blockchain: Algorand
* Smart Contracts: Python with PyTeal or Beaker
* Front-end: React.js with the Algorand JavaScript SDK(`algosdk`)
* Back-end (for API Gateway): Node.js with Express
* Decentralized Storage: IPFS (for storing encrypted verifiable credentials)
* Development Tools: AlgoKit CLI for local development, testing, and deployment.

How It Works:

1. A Community Health Worker (CHW) uses a mobile application to input basic birth information (Name, Date of Birth, Parents' Names).
2. The application hashes this data and sends an Application Call transaction to the Birth Registry Application on the Algorand blockchain.
3. The Algorand Application logs the transaction in its global state, recording the new individual's unique Decentralized Identifier (DID) and the data hash.
4. A Verifiable Credential (VC) (the birth certificate) is generated, encrypted, and stored on **IPFS**. The link to this encrypted file is stored in the Application's local    state for the individual's account.
5. The parents can access this VC via their secure digital wallet by signing a transaction to view the record.

Repository Structure

* `contracts/`: Python/PyTeal smart contracts for birth and health registries.
* `frontend/`: The React application for the community health worker and user dashboards.
* `test/`: Python/PyTest unit tests for the smart contracts.
* `docs/`: Detailed project documentation, diagrams, and user flows.
* `backend/`: Node.js server to interact with the Algorand blockchain and IPFS.

Credits and License

This project is a submission for "AlgoBharat Road to Impact Hack Series #2" . It is open-source under the MIT License. Feel free to fork, modify, and contribute!
