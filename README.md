# CS547Project
first run the following command to download data

```bash
bash ./datasets/download_cyclegan_dataset.sh horse2zebra
```

then go to *train_model.pbs*, modify the following line
```bash
aprun -n 1 -N 1 python train.py --dataroot ./datasets/horse2zebra --name horses_cyclegan --model cycle_gan --ngf 64 --ndf 64 --netG resnet9_blocks --init_type orthogonal --batch_size 1 --lr 0.0002 --lr_policy step --lambda_A 10 --lambda_B 10
```


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
