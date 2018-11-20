"""Paint Wizard

calculate which of following 3 products are cheapest to buy for the
room size
"""
import pandas
import Paints


def paint_wizard(room_size: int):
    paints_store = []
    paints_waste = []
    cheapo = Paints.CheapoMax()
    average = Paints.AverageJoes()
    dulux = Paints.DuluxourousPaints()
    paints_store.append((cheapo.name, cheapo.price, covered(room_size, cheapo.litre, cheapo.coverage)))
    paints_store.append((dulux.name, dulux.price, covered(room_size, dulux.litre, dulux.coverage)))
    paints_store.append((average.name, average.price, covered(room_size, average.litre, average.coverage)))

    paints_waste.append((cheapo.name, waste(room_size, cheapo.litre, cheapo.coverage)))
    paints_waste.append((average.name, waste(room_size, average.litre, average.coverage)))
    paints_waste.append((dulux.name, waste(room_size, dulux.litre, dulux.coverage)))

    info = pandas.DataFrame(data=paints_store,
                            columns=['Paint Names', 'Price', 'Coverage'])
    print(info, end="\n\n")

    waste_info = pandas.DataFrame(data=paints_waste,
                                  columns=['Paint Names', 'Waste'])
    print(waste_info, end="\n\n")


def covered(room_size: int, litre: int, coverage: int):
    paint_coverage = (coverage * litre) / room_size
    if paint_coverage > 0:
        return paint_coverage
    else:
        total = (((room_size / coverage) / litre) % litre) * price
        return total


def waste(room_size: int, litre: int, coverage: int):
    paint_waste = ((litre * coverage) - room_size) / coverage
    if paint_waste > 0:
        return paint_waste
    else:
        paint_needed = litre - ((room_size - (litre * coverage)) / coverage)
        return paint_needed


paint_wizard(20)
