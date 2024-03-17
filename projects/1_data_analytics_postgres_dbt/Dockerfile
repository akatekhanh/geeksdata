FROM python:3.10

WORKDIR /dbt

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Make .dbt folder
RUN mkdir -p /root/.dbt

COPY profiles.yml /root/.dbt/
COPY . .

WORKDIR /dbt/postgres_with_dbt

CMD [ "dbt", "debug" ]
