Install [the Python client](https://github.com/replicate/replicate-python):

```shell
pip install replicate
```

Next, [copy your API token](https://replicate.com/account) and authenticate by setting it as an environment variable:

```shell
export REPLICATE_API_TOKEN=r8_8iE**********************************
```

(This is your `Default` [API token](https://replicate.com/account/api-tokens). Keep it to yourself.)

Then, run the model:

```python
import replicate
output = replicate.run(
    "yorickvp/llava-13b:c293ca6d551ce5e74893ab153c61380f5bcbd80e02d49e08c582de184a8f6c83",
    input={"image": open("path/to/file", "rb")}
)
print(output)
```

To learn more, [take a look at the guide to get started with Python](https://replicate.com/docs/get-started/python).

[

#### Inputs

](https://replicate.com/yorickvp/llava-13b/versions/c293ca6d551ce5e74893ab153c61380f5bcbd80e02d49e08c582de184a8f6c83/api?tab=python#inputs)

- [
    
    ##### `image` _file_
    
    ](https://replicate.com/yorickvp/llava-13b/versions/c293ca6d551ce5e74893ab153c61380f5bcbd80e02d49e08c582de184a8f6c83/api?tab=python#input-image)
    
    Input image
    
- [
    
    ##### `prompt` _string_
    
    ](https://replicate.com/yorickvp/llava-13b/versions/c293ca6d551ce5e74893ab153c61380f5bcbd80e02d49e08c582de184a8f6c83/api?tab=python#input-prompt)
    
    Prompt to use for text generation
    
- [
    
    ##### `temperature` _number_
    
    ](https://replicate.com/yorickvp/llava-13b/versions/c293ca6d551ce5e74893ab153c61380f5bcbd80e02d49e08c582de184a8f6c83/api?tab=python#input-temperature)
    
    Temperature for text generation
    
    Default value: `0.2`
    
- [
    
    ##### `max_tokens` _integer_
    
    ](https://replicate.com/yorickvp/llava-13b/versions/c293ca6d551ce5e74893ab153c61380f5bcbd80e02d49e08c582de184a8f6c83/api?tab=python#input-max_tokens)
    
    Maximum number of tokens to generate
    
    Default value: `1024`
    

[

#### Output schema

](https://replicate.com/yorickvp/llava-13b/versions/c293ca6d551ce5e74893ab153c61380f5bcbd80e02d49e08c582de184a8f6c83/api?tab=python#output-schema)

This is the raw JSON schema describing the model's ouput structure.

```json
{
  "type": "string",
  "title": "Output"
}
```