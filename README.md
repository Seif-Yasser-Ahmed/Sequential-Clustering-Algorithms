# Sequential Clustering Algorithm

This repository contains an implementation of Basic Sequential Clustering Algorithms (BSAS and MBSAS) from scratch. These algorithms are used for clustering data points based on their proximity, using methods such as Euclidean and Manhattan distances, storing outputs in json files and visualizing them.

---

## Table of Contents

- [Directory Structure](#directory-structure)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [License](#license)

---

## Directory Structure

```plaintext
Seif-Yasser-Ahmed-Sequential-Clustering-Algorithms/
├── main.py
├── PyClustering.py
├── LICENSE
├── README.md
├── Src/
│   ├── distances.py
│   ├── Logger.py
│   ├── .gitignore
│   ├── __init__.py
│   ├── NumpyEncoder.py
│   ├── BSAS.py
│   └── MBSAS.py
└── Output/
    ├── clusters_BSAS_euclidean.json/.png
    ├── clusters_BSAS_manhattan.json/.png
    ├── clusters_MBSAS_manhattan.json/.png
    └── clusters_MBSAS_euclidean.json/.png
```

---

## Features

- **Clustering Algorithms:** Implementation of BSAS and MBSAS.
- **Distance Metrics:** Supports Euclidean and Manhattan distances.
- **Custom Logging:** Saves clustering results as JSON and visualizes clusters using matplotlib.
- **JSON Serialization:** Encodes numpy arrays into JSON format for saving and reusability.
- **Visualizing Clusters:** Encodes numpy arrays into JSON format for saving and reusability.

---

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.8 or later
- Required Python libraries:
  ```bash
  pip install numpy matplotlib pyclustering
  ```

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Seif-Yasser-Ahmed/Sequential-Clustering-Algorithms.git
   ```
2. Navigate to the directory:
   ```bash
   cd Sequential-Clustering-Algorithms
   ```

---

## Usage

### Running the Clustering Algorithm

To execute the clustering algorithms, run the `main.py` script:

```bash
python main.py
```

This will perform clustering using BSAS and MBSAS with Euclidean and Manhattan distances and save the results in the `Output/` directory as JSON files. It will also generate cluster visualizations.

### Example Output

The clustering results are stored in JSON files such as `clusters_BSAS_euclidean.json`. Below is an example of a cluster:

```json
[
    {
        "Cluster": 1,
        "Members": [
            [2, 3],
            [2, 5],
            [1, 4]
        ],
        "Mean": [
            1.67,
            4.0
        ]
    }
]
```

### Additional Script: PyClustering Integration

The `PyClustering.py` script compares the custom implementation with the `pyclustering` library for validation.

To run the comparison:
```bash
python PyClustering.py
```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

