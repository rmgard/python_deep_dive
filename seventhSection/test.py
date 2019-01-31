def val_summary(func):

    def wrapper(*args, **kwargs):

        data = func(*args, **kwargs)
        
        if len(data["summary"]) > 80:
            raise ValueError("Summary is too long")
        return data

    return wrapper

@val_summary
def fetch_customer_data():
    pass
