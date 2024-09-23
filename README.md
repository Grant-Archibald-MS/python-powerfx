# Python PowerFx

Example repository to demonstrate how to call PowerFx from python

## Getting started

1. Ensure .Net 8.0 SDK installed

2. Change to PowerFx module

```bash
cd src/PowerFx
```

3. Publish the example Power Fx class

```bash
dotnet publish -c Release  -r win-x64 --sc
```

4. Change to Python code and install dependancies

```
cd ..
pip install -r requirements.txt
```

5. Run the app

```
python main.py
```
