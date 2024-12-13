import click
from aemet.configuration.cli.configuration_cli import configuration
from aemet.alerts.cli.alert_cli import alert
from aemet.climatology.cli.climatology_cli import climatology

@click.group()
@click.version_option(version="1.0.0", prog_name="AEMET CLI")
def aemet():
    pass

aemet.add_command(configuration)
aemet.add_command(alert)
aemet.add_command(climatology)
