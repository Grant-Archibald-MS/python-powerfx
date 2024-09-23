using Microsoft.PowerFx;
using System.Collections;
using System.Threading;
using System.Threading.Tasks;

namespace PowerFx {
    public class PythonPowerFx
    {
        private static RecalcEngine Engine {get;set;}
        
        public async Task<object> Init(string config)
        {
            Engine = new RecalcEngine();
            return true;
        }

        public async Task<object> Evaluate(string text)
        {
            var result = await (Engine.EvalAsync(text, CancellationToken.None));
            return result.ToObject();
        }
    }
}