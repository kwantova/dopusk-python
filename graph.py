import matplotlib.pyplot as plt
import alg
import tukey


def custom_tukey(lw, lq, median, uq, uw):
    """
    Строит диаграмму Тьюки вручную по данным:
    lw - нижний ус,
    lq - нижний квартиль,
    median - медиана,
    uq - верхний квартиль,
    uw - верхний ус,
    """

    bw = 0.3  # Ширина ящика
    bc = 'lightgreen'
    lc = 'green'

    x_center = 1
    plt.figure()

    # координваты ящика
    x = [x_center - bw / 2, x_center + bw / 2, x_center + bw / 2, x_center - bw / 2]
    y = [lq, lq, uq, uq]

    # ящик
    plt.fill(x, y, color = bc, edgecolor = lc)

    # медиана
    plt.plot([x_center - bw / 2, x_center + bw / 2], [median, median], color = lc)

    # нижний ус (линия до нижнего квартиля)
    plt.plot([x_center, x_center], [lw, lq], color = lc)

    # верхний ус
    plt.plot([x_center, x_center], [uq, uw], color = lc)

    # черточки на концах усов
    plt.plot([x_center - bw / 2, x_center + bw / 2], [lw, lw], color = lc)
    plt.plot([x_center - bw / 2, x_center + bw / 2], [uw, uw], color = lc)

    # Настройка осей и меток
    plt.xlim(0.5, 1.5)  # Диапазон x для одной диаграммы
    plt.ylabel("Значения")
    plt.title("Диаграмма Тьюки")

    plt.show()
