# CS547Project
1.first run the following command to download data

```bash
bash ./datasets/download_cyclegan_dataset.sh horse2zebra
```

2. modify horse_script.pbs line 10 to correct local address 

3. submit horst_script to BW

The following are parameters you can adjust when training`

| parameter name     | meaning                                                          | possible value                                                      |
|--------------------|------------------------------------------------------------------|---------------------------------------------------------------------|
| ngf                | number of generator filters                                      | any positive integer                                                |
| ndf                | number of discriminator filters                                  | any positive integer                                                |
| netG               | architecture of Generator                                        | choose from [resnet_9blocks | resnet_6blocks | unet_256 | unet_128] |
| init_type          | parameter initialization method                                  | choose from [normal | xavier | kaiming | orthogonal]                |
| batch_size         |                                                                  |                                                                     |
| lr                 | learning rate                                                    | any meaningful float                                                |
| lr_policy          | policy to update learning rate                                   | choose from [linear | step | plateau | cosine]                      |
| lambda_A, lambda_B | regularization term in loss function. should keep these two same | any meaningful integer                                              |
