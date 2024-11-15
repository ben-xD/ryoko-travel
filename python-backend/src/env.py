from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class EnvSchema(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', 
                                env_file_encoding='utf-8')
    
    OPENAI_API_KEY: str = Field(None, min_length=1)
    LUMAAI_API_KEY: str = Field(None, min_length=1)
    CLOUDFLARE_R2_ACCESS_KEY_ID: str = Field(None, min_length=1)
    CLOUDFLARE_R2_ACCESS_KEY_SECRET: str = Field(None, min_length=1)
    CLOUDFLARE_ACCOUNT_ID: str = Field(None, min_length=1)
    ELEVENLABS_AGENT_ID: str = Field(None, min_length=1)
    ELEVENLABS_API_KEY: str = Field(None, min_length=1)
    
env = EnvSchema() # type: ignore [call-arg]

if __name__ == "__main__":
    print(env.model_dump())