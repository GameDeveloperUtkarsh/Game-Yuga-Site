name: Send Email

on:
  workflow_dispatch:
    inputs:
      name:
        description: "Sender's name"
        required: true
      email:
        description: "Sender's email address"
        required: true
      body:
        description: "Message body"
        required: true

jobs:
  send_mail_job:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Send email
        env:
          SENDER_EMAIL: ${{ secrets.SENDER_EMAIL }}
          EMAIL_PASSWORD: ${{ secrets.EMAIL_PASSWORD }}
          RECEIVER_EMAIL: ${{ secrets.RECEIVER_EMAIL }}
        run: |
          python "python codes/send_email.py" \
            "${{ github.event.inputs.name }}" \
            "${{ github.event.inputs.email }}" \
            "${{ github.event.inputs.body }}"
