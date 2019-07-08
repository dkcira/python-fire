#!/usr/bin/env python3
# grouping commands
import fire

class IngestionStage(object):

    def run(self):
        return 'Ingesting! Nom nom nom ...'

class DigestionStage(object):

    def run(self, volume=1):
        return ' '.join(['Burp!'] * volume)
    
    def status(self):
        return 'Satiated'

class Pipeline(object):

    def __init__(self):
        print('Pipeline initialization')
        self.ingestion = IngestionStage()
        self.digestion = DigestionStage()

    def run(self):
        print('Pipeline run')
        self.ingestion.run()
        self.digestion.run()

if __name__ == '__main__':
    fire.Fire(Pipeline)