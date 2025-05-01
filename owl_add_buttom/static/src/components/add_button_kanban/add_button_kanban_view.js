import { registry } from "@web/core/registry";
import { kanbanView } from "@web/views/kanban/kanban_view"
import { ProductPriceKanbanController } from "./add_button_kanban_controller";

export const productPricekanbanView = {
    ... kanbanView,
    Controller: ProductPriceKanbanController,
    buttonTemplate: "owl_add_buttom.KanbanView.Buttons",

};

registry.category("views").add("product_price_kanban", productPricekanbanView);
