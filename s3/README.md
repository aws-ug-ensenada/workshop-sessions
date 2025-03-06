# How to use the resources

## Deploy the infra

`tofu init`

`tofu plan`

`tofu apply`

`tofu destroy`

## How delete and upload local files to s3

`aws s3 rm s3://static-website-ens3625 --recursive`

`aws s3 cp ./s3/game/ s3://static-website-ens3625/ --recursive`