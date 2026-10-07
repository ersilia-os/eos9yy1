# Human Liver Cytosolic Stability

Estimates susceptibility to metabolism by enzymes in the liver cytosol, a route often overlooked because routine screening uses microsomal fractions instead. Shah and co-workers screened 1,450 compounds in human and mouse cytosol, treating a half-life at or below 30 minutes as unstable, and combined matched molecular pair analysis with QSAR modelling to derive transformation rules that were then tested experimentally on 125 compound pairs. The training set is skewed towards stable compounds, and accuracy fell sharply on an external library lying outside its applicability domain.

This model was incorporated on 2023-03-01.Last packaged on 2026-08-06.

## Information
### Identifiers
- **Ersilia Identifier:** `eos9yy1`
- **Slug:** `ncats-hlcs`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Activity prediction`
- **Biomedical Area:** `ADMET`
- **Target Organism:** `Homo sapiens`
- **Tags:** `ADME`, `Metabolism`, `Half-life`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1`
- **Output Consistency:** `Fixed`
- **Interpretation:** Probability of rapid turnover in human liver cytosol, with unstable meaning a half-life at or below 30 minutes.

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
- **Environment Size (Mb):** `2443`
- **Image Size (Mb):** `2625.95`

**Computational Performance (seconds):**
- 10 inputs: `25.87`
- 100 inputs: `15.79`
- 10000 inputs: `88.33`

### References
- **Source Code**: [https://github.com/ncats/ncats-adme](https://github.com/ncats/ncats-adme)
- **Publication**: [https://doi.org/10.1186/s13321-020-00426-7](https://doi.org/10.1186/s13321-020-00426-7)
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
