from day_13 import get_data_from_input, time_til_next_departure


def find_timestamp_with_desired_offset(current_timestamp, bus_id, current_offset, desired_offset, increment):
    """Advance by increment until current offset --> desired offset for bus ID"""
    timestamp = current_timestamp
    while current_offset != desired_offset:
        timestamp += increment
        current_offset = time_til_next_departure(timestamp, bus_id)
    return timestamp


def get_earliest_timestamp(bus_id_strs):
    bus_id_offset_tuples = []
    for idx, bus_id_str in enumerate(bus_id_strs):
        if bus_id_str != "x":
            bus_id = int(bus_id_str)
            bus_id_offset_tuples.append((bus_id, idx % bus_id))

    bus_id_offset_tuples.sort()
    bus_id, bus_id_offset = bus_id_offset_tuples.pop()
    print(f"Finding starting timestamp for bus ID {bus_id} with offset {bus_id_offset}")
    timestamp = 2 * bus_id - bus_id_offset
    increment = bus_id
    print(f"Starting timestamp is {timestamp}; starting increment is {increment}")
    while bus_id_offset_tuples:
        # Now find the next timestamp which fulfills the next largest bus ID
        bus_id, bus_id_offset = bus_id_offset_tuples.pop()
        print(f"Finding valid timestamp for bus ID {bus_id} with offset {bus_id_offset}")
        timestamp = find_timestamp_with_desired_offset(
            current_timestamp=timestamp,
            bus_id=bus_id,
            current_offset=time_til_next_departure(timestamp, bus_id),
            desired_offset=bus_id_offset,
            increment=increment,
        )
        increment *= bus_id
        print(f"Found valid timestamp {timestamp}; new increment is {increment}")
    return timestamp


if __name__ == "__main__":
    _, bus_ids = get_data_from_input()
    print(get_earliest_timestamp(bus_ids))
