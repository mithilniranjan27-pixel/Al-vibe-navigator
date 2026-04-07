if __name__ == "__main__":
    # host MUST be 0.0.0.0 and port MUST be 8080
    uvicorn.run(app, host="0.0.0.0", port=8080)
