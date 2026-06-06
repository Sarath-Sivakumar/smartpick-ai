def generate_response(
    query,
    retrieved_results
):

    response = []

    response.append(
        f"Question: {query}\n"
    )

    response.append(
        "Recommended Phones:\n"
    )

    for rank, (_, phone) in enumerate(
        retrieved_results,
        start=1
    ):

        response.append(
            f"{rank}. {phone['name']}"
        )

        response.append(
            f"   Price: ₹{phone['price']}"
        )

        response.append(
            f"   Camera: {phone['camera']}"
        )

        response.append(
            f"   Battery: {phone['battery']}"
        )

        response.append(
            f"   Gaming: {phone['gaming']}"
        )

        response.append(
            f"   Processor: {phone['processor']}"
        )

        response.append("")

    return "\n".join(response)