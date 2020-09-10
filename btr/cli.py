#!/bin/env python3

# Imports
import click

# Default command groups, usually display help
@click.group()
def cli():
  pass

# Start a service
@cli.command()
@click.argument('service')
def start(service):
    click.echo(f'Start service: {service}')

# Stop a service
@cli.command()
@click.argument('service')
def stop(service):
    click.echo(f'Stop service: {service}')

if __name__ == "__main__":
  cli()

