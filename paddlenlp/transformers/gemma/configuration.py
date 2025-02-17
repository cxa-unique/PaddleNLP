# Copyright (c) 2024 PaddlePaddle Authors. All Rights Reserved.
# Copyright 2024 EleutherAI and the HuggingFace Inc. team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
""" Gemma model configuration"""

from paddlenlp.transformers.configuration_utils import PretrainedConfig

__all__ = [
    "GEMMA_PRETRAINED_INIT_CONFIGURATION",
    "GemmaConfig",
    "GEMMA_PRETRAINED_RESOURCE_FILES_MAP",
]

GEMMA_PRETRAINED_INIT_CONFIGURATION = {
    "google/gemma-2b": {
        "architectures": ["GemmaForCausalLM"],
        "hidden_size": 2048,
        "initializer_range": 0.02,
        "intermediate_size": 16384,
        "max_position_embeddings": 8192,
        "model_type": "gemma",
        "num_attention_heads": 8,
        "num_key_value_heads": 1,
        "num_hidden_layers": 28,
        "rms_norm_eps": 1e-06,
        "vocab_size": 256000,
        "bos_token_id": 2,
        "eos_token_id": 1,
        "pad_token_id": 0,
        "use_cache": True,
        "use_recompute": False,
        "use_flash_attention": False,
    },
}


GEMMA_PRETRAINED_RESOURCE_FILES_MAP = {
    "model_state": {
        "google/gemma-2b": "https://bj.bcebos.com/paddlenlp/models/community/google/gemma-2b/model.safetensors",
        "google/gemma-2b-it": "https://bj.bcebos.com/paddlenlp/models/community/google/gemma-2b-it/model.safetensors",
    },
}


class GemmaConfig(PretrainedConfig):
    r"""
    This is the configuration class to store the configuration of a [`~GemmaModel`]. It is used to instantiate a gemma
    model according to the specified arguments, defining the model architecture. Instantiating a configuration with the
    defaults will yield a similar configuration to that of the Gemma-7B.
    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.
    Args:
        vocab_size (`int`, *optional*, defaults to 32000):
            Vocabulary size of the Gemma model. Defines the number of different tokens that can be represented by the
            `inputs_ids` passed when calling [`~GemmaModel`]
        hidden_size (`int`, *optional*, defaults to 4096):
            Dimension of the hidden representations.
        intermediate_size (`int`, *optional*, defaults to 11008):
            Dimension of the MLP representations.
        num_hidden_layers (`int`, *optional*, defaults to 32):
            Number of hidden layers in the Transformer encoder.
        num_attention_heads (`int`, *optional*, defaults to 32):
            Number of attention heads for each attention layer in the Transformer encoder.
        hidden_act (`str` or `function`, *optional*, defaults to `"silu"`):
            The non-linear activation function (function or string) in the decoder.
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        rms_norm_eps (`float`, *optional*, defaults to 1e-12):
            The epsilon used by the rms normalization layers.
        use_cache (`bool`, *optional*, defaults to `True`):
            Whether or not the model should return the last key/values attentions (not used by all models). Only
            relevant if `config.is_decoder=True`.
        tie_word_embeddings(`bool`, *optional*, defaults to `False`):
            Whether to tie weight embeddings
        use_fused_rope(`bool`, *optional*, defaults to False):
            Enable rope fusion or not.
        num_key_value_heads (`int`, *optional*):
            This is the number of key_value heads that should be used to implement Grouped Query Attention. If
            `num_key_value_heads=num_attention_heads`, the model will use Multi Head Attention (MHA), if
            `num_key_value_heads=1 the model will use Multi Query Attention (MQA) otherwise GQA is used. When
            converting a multi-head checkpoint to a GQA checkpoint, each group key and value head should be constructed
            by meanpooling all the original heads within that group. For more details checkout [this
            paper](https://arxiv.org/pdf/2305.13245.pdf). If it is not specified, will default to
            `num_attention_heads`.
        Example:
    ```python
    >>> from paddlenlp.transformer import GemmaModel, GemmaModel

    >>> # Initializing a Gemma gemma-7b style configuration
    >>> configuration = GemmaModel()

    >>> # Initializing a model from the gemma-7b style configuration
    >>> model = GemmaModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```"""
    model_type = "gemma"
    keys_to_ignore_at_inference = ["past_key_values"]

    def __init__(
        self,
        vocab_size=256000,
        hidden_size=3072,
        intermediate_size=24576,
        num_hidden_layers=28,
        num_attention_heads=16,
        num_key_value_heads=16,
        head_dim=256,
        hidden_act="gelu",
        max_position_embeddings=8192,
        seq_length=8192,
        initializer_range=0.02,
        rms_norm_eps=1e-6,
        use_cache=True,
        use_recompute=False,
        recompute_granularity="full",
        pad_token_id=0,
        eos_token_id=1,
        bos_token_id=2,
        tie_word_embeddings=True,
        rope_theta=10000.0,
        attention_bias=False,
        attention_dropout=0.0,
        tensor_parallel_output=True,
        sequence_parallel=False,
        fuse_sequence_parallel_allreduce=False,
        use_fused_rope=False,
        fuse_attention_qkv=False,
        fuse_attention_ffn=False,
        alibi=False,
        pp_recompute_interval=1,
        no_recompute_layers=None,
        use_flash_attention=False,
        use_fused_rms_norm=False,
        virtual_pp_degree=1,
        rope_scaling_factor=1.0,
        rope_scaling_type=None,
        **kwargs,
    ):
        self.vocab_size = vocab_size
        self.max_position_embeddings = max_position_embeddings
        self.seq_length = seq_length
        self.hidden_size = hidden_size
        self.intermediate_size = intermediate_size
        self.num_hidden_layers = num_hidden_layers
        self.num_attention_heads = num_attention_heads
        self.head_dim = head_dim
        self.num_key_value_heads = num_key_value_heads
        self.hidden_act = hidden_act
        self.initializer_range = initializer_range
        self.rms_norm_eps = rms_norm_eps
        self.use_cache = use_cache
        self.use_recompute = use_recompute
        self.recompute_granularity = recompute_granularity
        self.rope_theta = rope_theta
        self.attention_bias = attention_bias
        self.attention_dropout = attention_dropout
        self.tensor_parallel_output = tensor_parallel_output
        self.sequence_parallel = sequence_parallel
        self.fuse_sequence_parallel_allreduce = fuse_sequence_parallel_allreduce
        self.use_fused_rope = use_fused_rope
        self.fuse_attention_qkv = fuse_attention_qkv
        self.fuse_attention_ffn = fuse_attention_ffn
        self.alibi = alibi
        self.pp_recompute_interval = pp_recompute_interval
        self.no_recompute_layers = no_recompute_layers
        self.use_flash_attention = use_flash_attention
        self.use_fused_rms_norm = use_fused_rms_norm
        self.virtual_pp_degree = virtual_pp_degree
        self.rope_scaling_factor = rope_scaling_factor
        self.rope_scaling_type = rope_scaling_type
        super().__init__(
            pad_token_id=pad_token_id,
            bos_token_id=bos_token_id,
            eos_token_id=eos_token_id,
            tie_word_embeddings=tie_word_embeddings,
            tensor_parallel_output=tensor_parallel_output,
            **kwargs,
        )

    @property
    def rope(self):
        return not self.alibi
