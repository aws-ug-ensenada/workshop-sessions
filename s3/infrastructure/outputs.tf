output "bucket_name" {
    value = aws_s3_bucket.my_bucket.bucket
}

output "bucket_website_endpoint" {
    value = aws_s3_bucket_website_configuration.my_bucket_website.website_endpoint
}