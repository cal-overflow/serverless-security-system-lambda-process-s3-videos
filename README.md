# Video Processing Lambda Function
This lambda function is for the [serverless-security-system](https://github.com/cal-overflow/serverless-security-system).

The function parses over the contents of a given S3 bucket. The function will remove clips that do not include any motion.

## Helpful docs
  - [Creating lambda container image](https://docs.aws.amazon.com/lambda/latest/dg/images-create.html).

### Run container
```bash
docker run <tag_name>
```

### Environment variables (required)
- `S3_BUCKET`: The (unique) name of the S3 bucket to parse


# Setup (for deploying this image to ECR registry)
### 1. Create an IAM Role
In your AWS Account, create a new IAM Role with the permissions you deem necessary. The role must include permissions to create/update/delete resources in the following services.

  - [EC2 Container Registry](https://aws.amazon.com/sns/) - This can be achieved with `AmazonEC2ContainerRegistryFullAccess` policy.

### 2. Configure OpenID to connect AWS and GitHub Actions
Refer to GitHub's docs for [Configuring OpenID Connect in AWS](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services) for guidance.

### 3. Repository secrets
Add the following secrets via **Repository settings** > **Secrets** > **Actions**.

  - `IAM_ROLE_ARN` containing your IAM Role ARN from step 1.
