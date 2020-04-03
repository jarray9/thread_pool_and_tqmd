#!/bin/python
'''
pafyのドキュメンテーション : https://pythonhosted.org/pafy/
'''
import sys
import pafy


def download_audio(url):
    video = pafy.new(url)
    for au in video.audiostreams:
        au.download()

if __name__ == '__main__':
    if sys.argv[1:]:
        for url in sys.argv[1:]:
            download_audio(url)
