# Human Liver Cytosolic Stability

The human liver cytosol stability model is used for predicting the stability of a drug in the cytosol of human liver cells, which is beneficial for identifying potential drug candidates early during the drug discovery process. If a drug compound is quickly absorbed, it may not reach the intended target in the body or become toxic. On the other hand, if a drug compound is too stable, it could accumulate and cause detrimental effects. The authors use an NCATS dataset of 1450 compounds screened in vitro in mouse and human cytosol fractions. Compounds were classified as stable (half-life > 30min) or unstable (half-life ≤ 30 min). Note that authors report the dataset was biased towards stable compounds. The validation set of 250 compounds is openly available.

This model was incorporated on 2023-03-01.

## Information
### Identifiers
- **Ersilia Identifier:** `eos9yy1`
- **Slug:** `ncats-hlcs`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Activity prediction`
- **Biomedical Area:** `ADMET`
- **Target Organism:** `Homo sapiens`
- **Tags:** `ADME`, `Metabolism`, `Human`, `Half-life`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1`
- **Output Consistency:** `Fixed`
- **Interpretation:** Probability of a compound being unstable (half-life ≤ 30min) due to liver cells metabolism

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| hlcs_proba1 | float | high | Probability that a compound has a half-life of less than 30 minutes due to liver metabolism |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos9yy1](https://hub.docker.com/r/ersiliaos/eos9yy1)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos9yy1.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos9yy1.zip)

### Resource Consumption
- **Model Size (Mb):** `92`
- **Environment Size (Mb):** `2447`
- **Image Size (Mb):** `2526.83`

**Computational Performance (seconds):**
- 10 inputs: `33.49`
- 100 inputs: `23.35`
- 10000 inputs: `404.46`

### References
- **Source Code**: [https://github.com/ncats/ncats-adme](https://github.com/ncats/ncats-adme)
- **Publication**: [https://jcheminf.biomedcentral.com/articles/10.1186/s13321-020-00426-7](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-020-00426-7)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2020`
- **Ersilia Contributor:** [pauline-banye](https://github.com/pauline-banye)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [None](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos9yy1
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos9yy1
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
