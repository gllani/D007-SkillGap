def upload_to_s3(file_path, s3_file_name):
    """
    Placeholder for uploading a file to AWS S3.

    This is a non-functional stub that simulates the upload process
    for development environments where AWS is not yet configured.

    :param file_path: Path to the local file.
    :param s3_file_name: Target S3 file name (virtual, unused).
    :return: Dictionary simulating S3 upload response.
    """
    print(f"[DEV MODE] Simulating upload of '{file_path}' as '{s3_file_name}' to S3...")

    # Simulated S3 URL (not real)
    simulated_url = f"https://fake-s3-url.amazonaws.com/{s3_file_name}"

    return {
        "success": True,
        "message": "This is a simulated response. No real file was uploaded.",
        "s3_url": simulated_url
    }

# Example usage
if __name__ == "__main__":
    result = upload_to_s3("sample_resume.pdf", "uploads/sample_resume.pdf")
    print(result)
