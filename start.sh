#!/bin/bash
gunicorn library_project.wsgi:application