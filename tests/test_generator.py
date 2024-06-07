import pytest
from cyheadgen.generator import CythonHeaderGenerator


@pytest.fixture  # type: ignore[misc]
def cygen() -> CythonHeaderGenerator:
    return CythonHeaderGenerator()


def test_simple_generator(cygen: CythonHeaderGenerator) -> None:
    inp = """
    #ifndef API_H
    #define API_H

    Arguments *new_args(int interval, int time, char *name, int pid, int stats);
    Arguments *new_empty_args(void);
    DescriptorsArray *new_desc_array(void);
    DescriptorsArray generate_fd_stats_by_value(int pid, float interval,
                                                int time_limit);
    int literal_watch(float interval, int time, char *name, int pid, int stats);

    #endif // API_H"""

    assert (
        cygen(inp, header_name="core/api.h")
        == 'cdef extern from "core/api.h":\n\tArguments *new_args(int interval, int time, char* name, int pid, int stats)\n\tArguments *new_empty_args()\n\tDescriptorsArray *new_desc_array()\n\tDescriptorsArray generate_fd_stats_by_value(int pid, float interval, int time_limit)\n\tint literal_watch(float interval, int time, char* name, int pid, int stats)\n\t'
    )
