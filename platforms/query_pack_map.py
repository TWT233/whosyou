from platforms.query_pack import QueryPack
from platforms.steam import steam_query_pack

_query_pack_map: dict[str, QueryPack] = {
    'steam': steam_query_pack
}


def get_query_pack(platform: str) -> QueryPack:
    if platform not in _query_pack_map:
        raise ValueError(f'unknown platform: {platform}')
    return _query_pack_map[platform]
