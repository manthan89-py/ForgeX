# AI Junior Developer Test 
Welcome! You’ve stepped into the arena – now show us what you’ve got! 

## Mission
You're not just fiddling with code here; you're architecting the future. Your battleground? An AI app framework crying out for a brain.

Your task: Forge an 💬NLP chatbot that doesn’t just answer, but masters science-related questions.

Immerse yourself in the main.py file. Your battlefield is the execute function. Time to unleash your genius:
```python
############################################################
# Callback function called on each execution pass
############################################################
def execute(request: SimpleText, ray: Ray, state: State) -> SimpleText:
    output = []
    for text in request.text:
        # TODO Add code here
        response = 'Hello!' <<-- Here you add the magic 
        output.append(response)

    return SchemaUtil.create(SimpleText(), dict(text=output))
```
## Ground Rules
Step up with any arsenal (read: libraries or packages) you believe in, but remember:
* 👎 External services like chatGPT are off-limits. Stand on your own.
* 👎 Plagiarism is for the weak. Forge your own path.
* 👎 A broken app equals failure. Non-negotiable.

## Deployment Options
The application can be executed in two different ways:
* locally by running the `start.sh` 
* on in a docker container using `Dockerfile` 

## Proving Your Mettle
* Submit your masterpiece on GitHub. We want the link within **1 week, not a second more**.
* Go the extra mile and include a video where you walk us through your solution, showcasing 
it in live action. 
* We want to see not just what you've created but also how you envisioned and executed it


## This Is It
We're not just evaluating a project; we're judging your potential to revolutionize our 
landscape. A half-baked app won’t cut it.

We're zeroing in on:
* 👍 Exceptional documentation.
* 👍 Code that speaks volumes.
* 👍 Inventiveness that dazzles.
* 👍 A problem-solving beast.
* 👍 Unwavering adherence to the brief