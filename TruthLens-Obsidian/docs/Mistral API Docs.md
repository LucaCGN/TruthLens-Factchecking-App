## Create Chat Completions

##### Request Body Schema
`application/json`

**Required**

`model` (required)
: ID of the model to use. You can use the [List Available Models](https://docs.mistral.ai/api#operation/listModels) API to see all of your available models, or see our [Model overview](https://docs.mistral.ai/models) for model descriptions.

`messages` (required)
: Array of objects. The prompt(s) to generate completions for, encoded as a list of dictionaries with role and content. The first prompt role should be `user` or `system`.

- `role`: string (Enum: "system" "user" "assistant")
- `content`: string

`temperature`
: number or null [ 0 .. 1 ] (Default: 0.7) What sampling temperature to use, between 0.0 and 1.0. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. We generally recommend altering this or `top_p` but not both.

`top_p`
: number or null [ 0 .. 1 ] (Default: 1) Nucleus sampling, where the model considers the results of the tokens with `top_p` probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered. We generally recommend altering this or `temperature` but not both.

`max_tokens`
: integer or null >= 0 (Default: null) The maximum number of tokens to generate in the completion. The token count of your prompt plus `max_tokens` cannot exceed the model's context length.

`stream`
: boolean or null (Default: false) Whether to stream back partial progress. If set, tokens will be sent as data-only server-sent events as they become available, with the stream terminated by a data: [DONE] message. Otherwise, the server will hold the request open until the timeout or until completion, with the response containing the full result as JSON.

`safe_mode`
: boolean (Default: false) Whether to inject a safety prompt before all conversations.

`random_seed`
: integer (Default: null) The seed to use for random sampling. If set, different calls will generate deterministic results.
