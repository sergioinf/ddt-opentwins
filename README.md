# Distributed digital twins on the open-source OpenTwins framework

This repository contains the test scripts and data for the comparison of latency and resource consumption between two architectures, as described in the corresponding article.

## Test Descriptions

### Latency Comparison Test

This test aims to measure the difference between distributing the DTs and keeping the functions in the central server, also taking into account the difference in the ML
model’s inference time execution from the test PC and the cloud.

### Resource Consumption Test

To demonstrate that the new OpenTwins architecture really consumes fewer resources than the original one, the consumption of each architecture has been measured. All metrics were taken on the same equipment under the same circumstances and the result of the test is an average of 5 different data collections. These metrics are generated by the cluster itself thanks to the Google cAdvisor tool integrated in Kubernetes, and then stored in Prometheus for further study. These metrics provide detailed data on the resource consumption of running containers, covering aspects such as CPU, memory, network and storage usage.


Both test scripts has been used woth python 3.10 with the requierements in "requirements.txt".