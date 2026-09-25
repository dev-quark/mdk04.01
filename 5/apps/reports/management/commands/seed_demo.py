from decimal import Decimal

from django.core.management.base import BaseCommand

from apps.accounts.models import User
from apps.catalog.models import Brand, Car
from apps.clients.models import Client
from apps.orders.models import Order


class Command(BaseCommand):
    help = "Создаёт демонстрационные данные для практической работы №5"

    def handle(self, *args, **options):
        manager, _ = User.objects.get_or_create(
            username="manager",
            defaults={"first_name": "Иван", "last_name": "Менеджеров", "position": User.Position.MANAGER},
        )
        manager.set_password("manager12345")
        manager.save()

        admin, _ = User.objects.get_or_create(
            username="admin",
            defaults={"first_name": "Админ", "position": User.Position.ADMIN, "is_staff": True, "is_superuser": True},
        )
        admin.is_staff = True
        admin.is_superuser = True
        admin.set_password("admin12345")
        admin.save()

        toyota, _ = Brand.objects.get_or_create(name="Toyota", defaults={"country": "Япония"})
        bmw, _ = Brand.objects.get_or_create(name="BMW", defaults={"country": "Германия"})
        tesla, _ = Brand.objects.get_or_create(name="Tesla", defaults={"country": "США"})

        cars_data = [
            (toyota, "Camry", 2023, Decimal("4200000"), "JT000000000000001", Car.FuelType.PETROL),
            (toyota, "RAV4", 2024, Decimal("5100000"), "JT000000000000002", Car.FuelType.HYBRID),
            (bmw, "X5", 2023, Decimal("8900000"), "WB000000000000001", Car.FuelType.PETROL),
            (bmw, "3 Series", 2022, Decimal("6100000"), "WB000000000000002", Car.FuelType.PETROL),
            (tesla, "Model Y", 2024, Decimal("7200000"), "5Y000000000000001", Car.FuelType.ELECTRO),
        ]
        cars = []
        for brand, model, year, price, vin, fuel in cars_data:
            car, _ = Car.objects.get_or_create(
                vin=vin,
                defaults={
                    "brand": brand, "model": model, "year": year, "price": price,
                    "fuel_type": fuel, "status": Car.Status.AVAILABLE,
                },
            )
            cars.append(car)

        client1, _ = Client.objects.get_or_create(
            phone="+79990000001",
            defaults={"full_name": "Алексей Смирнов", "email": "alex@example.com", "manager": manager},
        )
        client2, _ = Client.objects.get_or_create(
            phone="+79990000002",
            defaults={"full_name": "Мария Орлова", "email": "maria@example.com", "manager": manager},
        )

        if not Order.objects.exists():
            order1 = Order.objects.create(
                client=client1, car=cars[0], manager=manager,
                order_type=Order.OrderType.PURCHASE,
                total_amount=cars[0].price,
            )
            order1.complete()
            order2 = Order.objects.create(
                client=client2, car=cars[2], manager=manager,
                order_type=Order.OrderType.PURCHASE,
                total_amount=cars[2].price,
            )
            order2.complete()
            Order.objects.create(
                client=client1, car=cars[1], manager=manager,
                order_type=Order.OrderType.TEST_DRIVE,
                total_amount=0,
            )

        self.stdout.write(self.style.SUCCESS("Демо-данные созданы."))
        self.stdout.write("Admin: admin / admin12345")
        self.stdout.write("Manager: manager / manager12345")
