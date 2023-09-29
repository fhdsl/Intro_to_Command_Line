import click

@click.group()
def cli():
    pass

#./bwa mem --ref [reference genome fasta file] --fastq [unaligned sequences fastq file]

@click.command()
@click.option('--ref', required=True, type=click.Path(exists=True), help='Reference genome FASTA file.')
@click.option('--fastq', required=True, type=click.Path(exists=True), help='Unaligned sequence FASTQ file.')
def mem(ref, fastq):
    with open(fastq) as f:
        i = 1
        j = 1
        for line in f:
            if i % 4 == 2:
                print("Aligned sequence ", j, ": ", line.strip())
                j += 1
            i += 1

@click.command()
def index():
    print("Indexing tool goes here.")

cli.add_command(mem)
cli.add_command(index)

if __name__ == '__main__':
    cli()