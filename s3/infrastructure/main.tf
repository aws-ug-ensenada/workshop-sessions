# filepath: /Ubuntu-24.04/home/jluna/projects/github/workshop-sessions/s3/infraestructure/main.tf
terraform {
    required_providers {
        aws = {
            source  = "hashicorp/aws"
            version = "5.89.0"
        }
    }
}

provider "aws" {
    region = "us-east-1"
}

## Create S3 bucket to host the static website
resource "aws_s3_bucket" "my_bucket" {
    bucket = "static-website-ens3625"
    tags = {
        Name        = "static-website-ens3625"
        Environment = "Dev"
    }
}

## Disable block public access
resource "aws_s3_bucket_public_access_block" "my_bucket_public_access_block" {
    bucket = aws_s3_bucket.my_bucket.id

    block_public_acls   = false
    block_public_policy = false
    ignore_public_acls  = false
    restrict_public_buckets = false
}

## Enable static website hosting
resource "aws_s3_bucket_website_configuration" "my_bucket_website" {
    bucket = aws_s3_bucket.my_bucket.id
    index_document {
        suffix = "index.html"
    }
    error_document {
        key = "error.html"
    }
}

## Create a bucket policy to allow public access
resource "aws_s3_bucket_policy" "my_bucket_policy" {
    bucket = aws_s3_bucket.my_bucket.bucket
    policy = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::${aws_s3_bucket.my_bucket.bucket}/*"
        }
    ]
}
EOF
}