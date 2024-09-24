import os
import sys
import asyncio
import clr
from pythonnet import load

sys.path.append(os.path.join(os.path.dirname(__file__), 'PowerFx/bin/Release/netstandard2.0/win-x64/publish'))

# Load the .Net Standard 2.0 compatible dll
clr.AddReference('PowerFx')

from System import Environment
from System import Type, Activator

# Initialize the PowerFx class using reflection
def init():
    power_fx_type = Type.GetType("PowerFx.PythonPowerFx, PowerFx")
    power_fx = Activator.CreateInstance(power_fx_type)
    init_method = power_fx_type.GetMethod("Init")
    init_method.Invoke(power_fx, [''])
    return power_fx

# Evaluate the input using PowerFx
async def evaluate(power_fx, input):
    power_fx_type = Type.GetType("PowerFx.PythonPowerFx, PowerFx")
    evaluate_method = power_fx_type.GetMethod("Evaluate")
    task = await asyncio.get_event_loop().run_in_executor(None, lambda: evaluate_method.Invoke(power_fx, [input]))
    result = task.Result
    return str(result)

# Main function
async def main():
    try:
        power_fx = init()
        loop = asyncio.get_event_loop()

        while True:
            input_text = input('> ')
            if input_text.lower() == 'exit' or input_text == '\x1A':  # '\x1A' is Control Z
                break
            try:
                result = await evaluate(power_fx, input_text)
                print(result)
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    asyncio.run(main())